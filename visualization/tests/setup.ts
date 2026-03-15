import '@testing-library/jest-dom/vitest';

import defs from '../public/defs.json';

import { vi } from 'vitest';

window.requestAnimationFrame = (callback: FrameRequestCallback): number => {
  return window.setTimeout(() => callback(performance.now()), 0);
};

const fetchDefs = (async (
  _input: URL | RequestInfo,
  _init?: RequestInit,
): Promise<Response> => {
  return new Response(JSON.stringify(defs), {
    headers: { 'Content-Type': 'application/json' },
  });
}) satisfies typeof fetch;

beforeEach(() => {
  localStorage.clear();
  vi.stubGlobal('fetch', fetchDefs);
});