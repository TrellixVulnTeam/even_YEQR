import React from "react";
import "./App.css";
import { FormA } from "./components/FormA";
import { Container } from "semantic-ui-react";
function App() {

  return (
    <Container style={{ marginTop: 40 }}>
      <FormA />
    </Container>
  );
}

export default App;
