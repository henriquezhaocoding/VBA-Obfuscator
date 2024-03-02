import random
import string
import re
import sys

def generate_unique_string(length=16):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))

def extract_modules_from_bas(file_path):
    with open(file_path, 'r') as file:
        vbs_code = file.read()

    # Use regular expressions to extract module names and content
    module_pattern = re.compile(r'^\s*Attribute\s+VB_Name\s*=\s*"([^"]+)"(?:.*?^End\s+Attribute)?\s*^(.*?^End\s+(?:Sub|Function|Property|Class))', re.MULTILINE | re.DOTALL)

    modules = []
    for match in module_pattern.finditer(vbs_code):
        module_name = match.group(1)
        module_content = match.group(2)
        modules.append((module_name, module_content))

    return modules

def obfuscate_module(file_path):
    modules = extract_modules_from_bas(file_path)

    obfuscated_modules = []

    for module_name, module_content in modules:
        obfuscated_code = module_content
        obfuscation_mapping = []

        for line in module_content.splitlines():
            # Your obfuscation logic here
            # Example: Replace variable names with unique strings
            for variable in re.findall(r'\b(?:Dim|Private|Public|Static)\s+(\w+)\b(?!\()', line):
                unique_string = generate_unique_string()
                obfuscated_code = re.sub(r'\b' + re.escape(variable) + r'\b', unique_string, obfuscated_code)
                obfuscation_mapping.append((variable, unique_string))

        obfuscated_modules.append((module_name, obfuscated_code, obfuscation_mapping))

    obfuscation_mapping_file = f"{file_path}_obfuscation_mapping.txt"
    obfuscated_code_file = f"{file_path}_obfuscated_code.txt"

    with open(obfuscation_mapping_file, 'w') as f:
        for module_name, mapping in zip(modules, obfuscated_modules):
            f.write(f"{module_name[0]}\n")
            for original, obfuscated in mapping[2]:
                f.write(f"{original}\t{obfuscated}\n")

    with open(obfuscated_code_file, 'w') as f:
        for module_name, obfuscated_code, _ in obfuscated_modules:
            f.write(f"{module_name}\n{obfuscated_code}\n")

# Example usage
abs_path = "\\".join(sys.argv[0].split("\\")[:-1])
file_path = abs_path + "\\Module1.bas"
obfuscate_module(file_path)

