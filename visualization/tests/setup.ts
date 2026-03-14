import '@testing-library/jest-dom/vitest';

import defs from '../public/defs.json';

import { vi } from 'vitest';

Object.defineProperty(HTMLElement.prototype, 'clientWidth', {
  configurable: true,
  get() {
    return 960;
  },
});

Object.defineProperty(HTMLElement.prototype, 'clientHeight', {
  configurable: true,
  get() {
    return 640;
  },
});

Object.defineProperty(SVGElement.prototype, 'clientWidth', {
  configurable: true,
  get() {
    return 960;
  },
});

Object.defineProperty(SVGElement.prototype, 'clientHeight', {
  configurable: true,
  get() {
    return 640;
  },
});

window.requestAnimationFrame = (callback: FrameRequestCallback): number => {
  return window.setTimeout(() => callback(performance.now()), 0);
};

window.cancelAnimationFrame = (id: number): void => {
  window.clearTimeout(id);
};

beforeEach(() => {
  localStorage.clear();
  vi.restoreAllMocks();
  vi.stubGlobal(
    'fetch',
    vi.fn(async () => ({
      json: async () => defs,
    })) as typeof fetch,
  );
});