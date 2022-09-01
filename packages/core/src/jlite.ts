import { JupyterLiteServer } from '@jupyterlite/server';
import type { MessageCallback } from './messaging';

const serverExtensions = [
  import('@jupyterlite/pyolite-kernel-extension'),
  import('@jupyterlite/server-extension'),
];

export async function startJupyterLiteServer(messsages?: MessageCallback) {
  const litePluginsToRegister: JupyterLiteServer.IPluginModule[] = [];

  /**
   * Iterate over active plugins in an extension.
   */
  function* activePlugins(extension: any) {
    // Handle commonjs or es2015 modules
    let exports;
    if (extension.hasOwnProperty('__esModule')) {
      exports = extension.default;
    } else {
      // CommonJS exports.
      exports = extension;
    }

    const plugins = Array.isArray(exports) ? exports : [exports];
    for (const plugin of plugins) {
      yield plugin;
    }
  }

  // Add the base serverlite extensions
  const baseServerExtensions = await Promise.all(serverExtensions);
  baseServerExtensions.forEach((p) => {
    for (const plugin of activePlugins(p)) {
      litePluginsToRegister.push(plugin);
    }
  });

  // create the in-browser JupyterLite Server
  const jupyterLiteServer = new JupyterLiteServer({} as any);
  jupyterLiteServer.registerPluginModules(litePluginsToRegister);
  // start the server
  await jupyterLiteServer.start();

  const { serviceManager } = jupyterLiteServer;
  await serviceManager.ready;

  return serviceManager;
}
