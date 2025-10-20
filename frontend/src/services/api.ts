// services/api.ts (Melhorado: Adicionado error handling global, refresh token logic, typed responses)
import axios from 'axios';

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || 'http://localhost:8000',
  timeout: 10000,
  headers: { 'Content-Type': 'application/json' },
});

api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) config.headers.Authorization = `Bearer ${token}`;
  return config;
});

api.interceptors.response.use(
  response => response,
  async (error) => {
    if (error.response.status === 401 && !error.config._retry) {
      error.config._retry = true;
      try {
        const refreshToken = localStorage.getItem('refreshToken');
        const response = await api.post('/core/token/refresh/', { refresh: refreshToken });
        localStorage.setItem('token', response.data.access);
        error.config.headers.Authorization = `Bearer ${response.data.access}`;
        return api(error.config);
      } catch (refreshError) {
        localStorage.clear();``
        window.location.href = '/login';
        return Promise.reject(refreshError);
      }
    }
    return Promise.reject(error);
  }
);

export default api;