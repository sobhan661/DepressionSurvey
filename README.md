# Depression Survey

A Django web application that provides a screening-oriented estimate based on self-reported social media use, sleep, activity, academic performance, and related habits. The application uses a scikit-learn model to generate a risk percentage and presents it as an informational screening result.

This project is a portfolio demonstration and is not a medical device, diagnostic tool, or substitute for professional mental-health care.

## Features

- Responsive survey interface
- Server-side form validation and CSRF protection
- Scikit-learn model inference through a cached Django view
- Screening result with an explicit non-diagnostic notice
- Production configuration for Gunicorn, WhiteNoise, HTTPS, PostgreSQL, and Render
- Health-check endpoint at `/health/`

## Technology

- Python 3.13
- Django 6
- scikit-learn and pandas
- Gunicorn
- WhiteNoise
- PostgreSQL in production
- Render

## Project structure

```text
.
├── ml/
│   ├── models/depression_classifier.joblib
│   └── src/train.py
├── webapp/
│   ├── core/
│   ├── templates/
│   ├── webapp/
│   └── manage.py
├── build.sh
├── render.yaml
└── requirements.txt
```

## Local setup

Create and activate a virtual environment, then install the dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Create `.env` from `.env.example` and use a local development secret:

```env
DJANGO_SECRET_KEY=replace-with-a-long-random-development-secret
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

Run migrations and start the development server:

```powershell
cd webapp
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in a browser.

## Testing

From the repository root, run:

```powershell
.\.venv\Scripts\python.exe webapp\manage.py test core
.\.venv\Scripts\python.exe webapp\manage.py check --deploy
```

## Deployment on Render

The repository includes `render.yaml`, which defines a Render Web Service and PostgreSQL database.

1. Push the repository to GitHub, including `ml/models/depression_classifier.joblib`.
2. In Render, select **New Blueprint Instance** and connect the repository.
3. Render reads `render.yaml`, provisions the service and database, installs dependencies, runs migrations, and starts Gunicorn.
4. Open the generated `onrender.com` URL after the deployment completes.

Render generates `DJANGO_SECRET_KEY` and configures production values automatically. Do not commit `.env` or add real credentials to `.env.example`.

For a custom domain, add the domain in Render and update `ALLOWED_HOSTS` and `CSRF_TRUSTED_ORIGINS` in the Render environment variables.

## Environment variables

| Variable | Purpose |
| --- | --- |
| `DJANGO_SECRET_KEY` | Required secret used by Django security features. |
| `DEBUG` | Use `True` locally and `False` in production. |
| `ALLOWED_HOSTS` | Comma-separated hostnames accepted by Django. |
| `CSRF_TRUSTED_ORIGINS` | Comma-separated trusted HTTPS origins for form submissions. |
| `DATABASE_URL` | PostgreSQL connection string used in production. |

## Important limitations

The output is a model-generated screening estimate, not a diagnosis or clinical recommendation. It should not be used to make medical decisions. Anyone experiencing distress or feeling unsafe should seek support from a qualified mental-health professional or local emergency service.

## License

No license has been specified for this repository. Add a license before distributing or reusing the project.
