import '@testing-library/jest-dom/vitest';

import { vi } from 'vitest';

window.requestAnimationFrame = (callback: FrameRequestCallback): number => {
  return window.setTimeout(() => callback(performance.now()), 0);
};

beforeEach(() => {
  localStorage.clear();
  vi.unstubAllGlobals();
});