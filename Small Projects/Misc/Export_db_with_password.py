import os

def generate_export_script(endpoint, username, oassword, databse):
    script = f'''\
#!/bin/bash
#Export data from RDS database
mysqldump -h (endpoint) -u (username) -p(password) (databse) > dump.sql
'''
    with open('export_script.sh', 'w') as f:
        f.write(script)
    os.chmod('export_script.sh', 0o755)

if __name__ == '__main__':
    endpoint = input('Enter RDS Endpoint: ')
    username = input('Enter username: ')
    password = input('Enter password: ')
    database = input('Enter database name: ')

    generate_export_script(endpoint, username, password, database)

    print('Export script generated: export_script.sh')

    os.system('chmod +x export_script.sh')

    # Execute the script file
    os.system('./export_script.sh')