import * as thebelab from "./thebelab";
export * from "./thebelab";
export * from "./utils";
import $ from "jquery";

document.addEventListener("DOMContentLoaded", () => {
  if (typeof window !== "undefined") {
    window.thebelab = thebelab;
    window.thebelab.$ = $;
    const options = thebelab.mergeOptions();
    if (options.mountStatusWidget) {
      thebelab.mountStatusWidget();
    }
    if (options.mountActivateWidget) {
      thebelab.mountActivateWidget();
    }
    if (options["bootstrap"]) {
      thebelab.bootstrap();
    }
  }
});
