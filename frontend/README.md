# Oyster Frontend

A modern Next.js application with TypeScript for the Oyster content curation platform.

## Tech Stack

- **Framework**: Next.js 14 with App Router
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **State Management**: Redux Toolkit
- **Data Fetching**: TanStack Query (React Query)
- **Animations**: Framer Motion
- **Icons**: Lucide React

## Getting Started

1. **Install dependencies**:

   ```bash
   npm install
   ```

2. **Run development server**:

   ```bash
   npm run dev
   ```

3. **Build for production**:

   ```bash
   npm run build
   npm start
   ```

4. **Type checking**:

   ```bash
   npm run type-check
   ```

5. **Linting**:
   ```bash
   npm run lint
   ```

## Project Structure

```
src/
├── app/                    # Next.js App Router
│   ├── layout.tsx         # Root layout
│   ├── page.tsx           # Home page
│   ├── globals.css        # Global styles
│   └── ...                # Other pages
├── components/            # Reusable components
│   ├── GeneralComp/       # General UI components
│   ├── LandingPageComp/   # Landing page components
│   ├── LoginComp/         # Authentication components
│   └── SignupComp/        # Registration components
├── lib/                   # Utility functions
├── types/                 # TypeScript type definitions
└── store/                 # Redux store configuration
```

## Key Features

- **Server-Side Rendering**: Optimized for SEO and performance
- **Type Safety**: Full TypeScript coverage
- **Responsive Design**: Mobile-first approach with Tailwind CSS
- **Modern UI**: Beautiful components with smooth animations
- **API Integration**: Seamless connection with Django backend

## Development Guidelines

- Use TypeScript for all new components
- Follow Next.js 13+ App Router conventions
- Use Tailwind CSS for styling
- Implement proper error boundaries
- Write comprehensive tests

## Deployment

The application is configured for deployment on Vercel, Netlify, or any Node.js hosting platform.

For production builds, ensure all environment variables are properly configured and the Django backend is accessible.
