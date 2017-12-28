class FileOwners:

    @staticmethod
    def group_by_owners(files):
        file_owner, file_name ={},[]
        for filename, owner in files.items():
            file_owner.setdefault(owner,[]).append(filename)
        return(file_owner)

files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy',
    '/etc/hosts': 'root',
    '/etc/shadow': 'root'
}

print(FileOwners.group_by_owners(files))