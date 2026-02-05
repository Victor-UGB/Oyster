# Oyster - Decentralized Content Curation Platform

Oyster is a Web3-powered platform that helps users curate, organize, and share valuable online content ("pearls") with intelligent AI assistance and decentralized social features.

## Architecture Overview

### Frontend

- **Framework**: Next.js 14 with TypeScript
- **Styling**: Tailwind CSS
- **State Management**: Redux Toolkit
- **Data Fetching**: TanStack Query

### Backend

- **Framework**: Django 3.2 with Django REST Framework
- **Database**: PostgreSQL
- **AI/ML**: Python-based services for content analysis
- **Blockchain**: Internet Computer Protocol (ICP) integration

### Key Features

- ✨ Intelligent content organization with AI
- 🌐 Decentralized social networking
- 💎 NFT integration for valuable content
- 🔔 Smart reminders and notifications
- 🎨 Beautiful, responsive UI
- 🔒 Web3 authentication and ownership

## Quick Start

### Prerequisites

- Node.js 18+
- Python 3.8+
- PostgreSQL
- Git

### Backend Setup

```bash
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Visit `http://localhost:3000` for the frontend and `http://localhost:8000` for the API.

## Project Structure

```
oyster/
├── frontend/              # Next.js TypeScript application
│   ├── src/
│   │   ├── app/          # App Router pages
│   │   ├── components/   # Reusable UI components
│   │   └── lib/          # Utilities and configurations
├── backend/               # Django REST API
│   ├── manage.py
│   ├── vecugoinc/        # Django settings
│   ├── Pearl/            # Core app
│   └── frontend/         # Django frontend app
├── docs/                  # Documentation
│   ├── PRD.md           # Product Requirements Document
│   └── Architecture.md  # Technical Architecture
└── README.md
```

## Development

### Frontend Development

```bash
cd frontend
npm run dev          # Start development server
npm run build        # Build for production
npm run type-check   # TypeScript checking
```

### Backend Development

```bash
cd backend
python manage.py runserver     # Start Django server
python manage.py makemigrations # Create migrations
python manage.py migrate       # Apply migrations
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Roadmap

- [ ] MVP Launch with core curation features
- [ ] AI-powered content recommendations
- [ ] Social features and community building
- [ ] Web3 integration and NFT marketplace
- [ ] Mobile application development

For detailed information, see our [Product Requirements Document](docs/PRD.md) and [Technical Architecture](docs/Architecture.md).
