import { useMemo, useState } from 'react';
import { ThebeCoreProvider, ThebeServerProvider } from 'thebe-react';
import { NavLink, Outlet } from 'react-router-dom';
import './App.css';
import { Connect } from './Connect';
import { ServerMode, ServerModeType } from './ServerMode';

function App() {
  const [mode, setMode] = useState<ServerModeType>('local');

  const options = useMemo(
    () => ({
      useBinder: false,
      kernelOptions: {
        name: 'Python 3',
      },
      savedSessionOptions: {
        enabled: false,
      },
    }),
    [],
  );

  return (
    <div className="App">
      <div className="my-6">
        <h1 className="text-3xl font-bold">Notebooks & Widgets</h1>
        <p>Available examples:</p>
        <div className="flex justify-center space-x-2">
          <NavLink
            className={({ isActive }) => (isActive ? 'font-semibold underline' : 'hover:underline')}
            to="/nb/widget-test"
          >
            widget basics
          </NavLink>
          <NavLink
            className={({ isActive }) => (isActive ? 'font-semibold underline' : 'hover:underline')}
            to="/nb/widget-test-ipympl"
          >
            ipympl
          </NavLink>
        </div>
      </div>
      <ThebeCoreProvider>
        <ThebeServerProvider
          connect={false}
          options={options}
          useBinder={false}
          useJupyterLite={mode === 'lite'}
        >
          <ServerMode mode={mode} setMode={setMode} />
          <Connect />
          <Outlet />
        </ThebeServerProvider>
      </ThebeCoreProvider>

      <div className="fixed top-2 right-1 text-xs">
        Server icon by Ralf Schmitzer from{' '}
        <a
          href="https://thenounproject.com/browse/icons/term/server/"
          target="_blank"
          title="Server Icons"
          rel="noreferrer"
        >
          Noun Project
        </a>
      </div>
    </div>
  );
}

export default App;