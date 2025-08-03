import os

# Define folders to create (including subfolders)
folders = [
    'app',
    'model/artifacts',
    'tests',
    'lambda',
    'ci_cd'
]

# Define files (relative to each folder)
files = {
    'app': ['main.py', 'model.py', 'schemas.py', 'config.py', 'requirements.txt'],
    'model': ['train.py', 'evaluate.py', 'config.yaml', 'requirements.txt'],
    'tests': ['test_prediction.py', 'test_training.py'],
    'lambda': ['lambda_function.py', 'config.py', 'requirements.txt'],
    'ci_cd': ['Dockerfile', 'github-actions.yml'],
    'root': ['.gitignore', 'README.md']
}

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create empty files in each folder
for folder, flist in files.items():
    if folder == 'root':
        for fname in flist:
            open(fname, 'a').close()
    else:
        for fname in flist:
            path = os.path.join(folder, fname)
            open(path, 'a').close()
