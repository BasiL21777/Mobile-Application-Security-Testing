import os
import xml.etree.ElementTree as ET

class ScanAndroidManifest(object):

    def __init__(self) -> None:
        pass

    def extract_manifest_info(self, extracted_source_path):
        manifest_path = os.path.join(extracted_source_path, "resources", "AndroidManifest.xml")
        
        if not os.path.isfile(manifest_path):
            print(f"[-] ERROR: Manifest file {manifest_path} not found.")
            return {}

        etparse = ET.parse(manifest_path)
        manifest = etparse.getroot()

        if not manifest:
            print(f"[-] ERROR: Error parsing the manifest file for {extracted_source_path}.")
            return {}

        android_namespace = '{http://schemas.android.com/apk/res/android}'
        components, exported_components = self.parse_android_manifest(manifest_path)

        data = {
            'platform_build_version_code': manifest.attrib.get('platformBuildVersionCode', "Not available"),
            'complied_sdk_version': manifest.attrib.get('compileSdkVersion', "Not available"),
            'permissions': [elem.attrib[f'{android_namespace}name'] for elem in manifest.findall('uses-permission')],
            'dangerous_permission': "",
            'package_name': manifest.attrib.get('package', "Not available"),
            'activities': [elem.attrib[f'{android_namespace}name'] for elem in manifest.findall('application/activity')],
            'exported_activity': exported_components['activity'],
            'services': [elem.attrib[f'{android_namespace}name'] for elem in manifest.findall('application/service')],
            'exported_service': exported_components['service'],
            'receivers': [elem.attrib[f'{android_namespace}name'] for elem in manifest.findall('application/receiver')],
            'exported_receiver': exported_components['receiver'],
            'providers': [elem.attrib[f'{android_namespace}name'] for elem in manifest.findall('application/provider')],
            'exported_provider': exported_components['provider'],
        }

        indent = "    "

        # Dangerous permissions list
        DANGEROUS_TYPES = [
            "android.permission.READ_CALENDAR",
            "android.permission.WRITE_CALENDAR",
            "android.permission.CAMERA",
            "android.permission.READ_CONTACTS",
            "android.permission.WRITE_CONTACTS",
            "android.permission.GET_ACCOUNTS",
            "android.permission.ACCESS_FINE_LOCATION",
            "android.permission.ACCESS_COARSE_LOCATION",
            "android.permission.RECORD_AUDIO",
            "android.permission.READ_PHONE_STATE",
            "android.permission.READ_PHONE_NUMBERS",
            "android.permission.CALL_PHONE",
            "android.permission.ANSWER_PHONE_CALLS",
            "android.permission.READ_CALL_LOG",
            "android.permission.WRITE_CALL_LOG",
            "android.permission.ADD_VOICEMAIL",
            "android.permission.USE_SIP",
            "android.permission.PROCESS_OUTGOING_CALLS",
            "android.permission.BODY_SENSORS",
            "android.permission.SEND_SMS",
            "android.permission.RECEIVE_SMS",
            "android.permission.READ_SMS",
            "android.permission.RECEIVE_WAP_PUSH",
            "android.permission.RECEIVE_MMS",
            "android.permission.READ_EXTERNAL_STORAGE",
            "android.permission.WRITE_EXTERNAL_STORAGE",
            "android.permission.MOUNT_UNMOUNT_FILESYSTEMS",
            "android.permission.READ_HISTORY_BOOKMARKS",
            "android.permission.WRITE_HISTORY_BOOKMARKS",
            "android.permission.INSTALL_PACKAGES",
            "android.permission.RECEIVE_BOOT_COMPLETED",
            "android.permission.READ_LOGS",
            "android.permission.CHANGE_WIFI_STATE",
            "android.permission.DISABLE_KEYGUARD",
            "android.permission.GET_TASKS",
            "android.permission.BLUETOOTH",
            "android.permission.CHANGE_NETWORK_STATE",
            "android.permission.ACCESS_WIFI_STATE",
        ]
        dangerous_permissions = [perm for perm in data['permissions'] if perm in DANGEROUS_TYPES]

        # Print results
        print("[+] Package Name:")
        print(indent + data['package_name'] + "\n")

        print("[+] Platform Build Version Code:")
        print(indent + str(data['platform_build_version_code']) + "\n")

        print("[+] Compile SDK Version:")
        print(indent + str(data['complied_sdk_version']) + "\n")

        if data['permissions']:
            print("[+] Permissions:")
            for permission in data['permissions']:
                print(indent + permission)
            print()
        
        if dangerous_permissions:
            print("[+] Dangerous Permissions:")
            data['dangerous_permission'] = dangerous_permissions
            for permission in dangerous_permissions:
                print(indent + permission)
            print()
        
        if data['activities']:
            print("[+] Activities:")
            for activity in data['activities']:
                print(indent + activity)
            print()
        
        if data['exported_activity']:
            print("[+] Exported Activities:")
            for activity in data['exported_activity']:
                print(indent + activity)
            print()

        if data['services']:
            print("[+] Services:")
            for service in data['services']:
                print(indent + service)
            print()
        
        if data['exported_service']:
            print("[+] Exported Services:")
            for activity in data['exported_service']:
                print(indent + activity)
            print()

        if data['receivers']:
            print("[+] Receivers:")
            for receiver in data['receivers']:
                print(indent + receiver)
            print()
        
        if data['exported_receiver']:
            print("[+] Exported Receivers:")
            for activity in data['exported_receiver']:
                print(indent + activity)
            print()

        if data['providers']:
            print("[+] Providers:")
            for provider in data['providers']:
                print(indent + provider)
            print()
        
        if data['exported_provider']:
            print("[+] Exported Providers:")
            for activity in data['exported_provider']:
                print(indent + activity)
            print()

        return data
    
    def is_exported(self, component, ns):
        return component.get(f"{{{ns['android']}}}exported") == "true"

    def parse_android_manifest(self, manifest_path):
        ns = {'android': 'http://schemas.android.com/apk/res/android'}
        etparse = ET.parse(manifest_path)
        root = etparse.getroot()

        components = {'activity': [], 'service': [], 'receiver': [], 'provider': []}
        exported_components = {'activity': [], 'service': [], 'receiver': [], 'provider': []}

        for component_type in components.keys():
            for component in root.findall(f".//{component_type}"):
                name = component.get(f"{{{ns['android']}}}name")
                components[component_type].append(name)
                if self.is_exported(component, ns):
                    exported_components[component_type].append(name)

        return components, exported_components
