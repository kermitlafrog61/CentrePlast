# CetrePlast test

## Setup

To get this project up and running on your local machine, follow these steps:

### Prerequisites

- Docker Engine and Compose plugin
- Python

### Installation

1. **Clone the Repository**

```bash
git clone https://github.com/CentrePlast.git
cd CentrePlast
```

2. **Write everything in .env**
```bash
cp .env.template .env
```
And then write everything in it

3. **Start Docker Compose**

```bash
docker compose up -d
```

4. **Create Superuser**

```bash
docker exec -it centreplast-backend-1 python manage.py createsuperuser
```

The site should now be running on http://127.0.0.1/.


## Usage

### Accessing the Site
Navigate to http://127.0.0.1/ in your web browser.

### Admin Interface
Access the Django admin by navigating to http://127.0.0.1/admin/. Log in with the superuser account to manage users and reports.

### Creating and Viewing Reports
After logging in, use the navigation bar to access different sections of the site:

Home: A welcome page with options to view or create reports based on user authentication status.
Monthly Revenue Report: Generate and view revenue summaries for selected months.
Reports: List, create, and update daily revenue reports.
Contributing
We welcome contributions to this project. Please open an issue for discussion before submitting a pull request.

