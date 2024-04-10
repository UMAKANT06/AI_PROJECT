import React from "react";
import { Switch, Route } from "react-router-dom";

import PageNotFound from "./components/PageNotFound/pageNotFound";
import { Game } from "./components/Game/index";

import { ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

function App() {
  return (
    <>

      <Switch>
        <Route path="/" component={Game} />
        <Route component={PageNotFound} />
      </Switch>
      <ToastContainer autoClose={2000} hideProgressBar />
    </>
  );
}

export default App;
