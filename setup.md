# Setup Guide — Rising-Waters

## Prerequisites

- Python 3.10 or higher
- Git
- Visual Studio Code (recommended)

## Step-by-Step Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Rising-Waters.git
cd Rising-Waters
```

### 2. Create a Virtual Environment

**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Upgrade pip

```bash
python -m pip install --upgrade pip
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Launch Jupyter Notebooks (Optional)

```bash
jupyter notebook
```

Then open the notebooks under the `notebooks/` directory.

### 6. Run the Flask App

```bash
python app/app.py
```

Visit `http://127.0.0.1:5000` in your browser.

## VS Code Extensions (Recommended)

- Python (Microsoft)
- Jupyter
- Pylance
- GitLens
- Markdown Preview Enhanced

## Dataset Setup

Place raw data files in `dataset/raw/`.  
Processed data will be saved to `dataset/processed/`.

## Model Storage

Trained models are saved to `models/`. This directory is gitignored; use the
`.gitkeep` file to preserve the folder structure in version control.
