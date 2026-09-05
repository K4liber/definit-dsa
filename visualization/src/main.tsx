import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import { BrowserRouter } from 'react-router-dom';
import App from './App';
import './App.css';

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    {/* Only the query string is used for filters, so BrowserRouter works on
        GitHub Pages without any 404.html fallback. */}
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </StrictMode>,
);
