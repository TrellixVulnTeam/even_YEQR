import React, { useEffect, useState } from "react";
import axios from "axios";
import { Form, Input, Button } from "semantic-ui-react";
import { TabelA } from "./TabelA";

export const FormA = () => {
  const [ip, ipSet] = useState("");
  const [uname, unameSet] = useState("");
  const [pwd, pwdSet] = useState("");
  const [load, loadingSet] = useState(false);
  const [psaux, psauxSet] = useState("");

  useEffect(() => {
    loadingSet(true);
    axios.get("http://127.0.0.1:5000/request").then((x) => {
      let xx = x.data;
      console.log(xx);
      let xxx = xx.slice(1);
      console.log(xxx);
      let x4 = xxx[0];
      console.log(x4);
      let x5 = x4.trim()
      console.log(x5);
      let x6 = Array.from(x5.split("\n"));
      console.log(x6);
      psauxSet(x6);
      console.log(psaux);
      loadingSet(false);
    });
  }, []);
  //
  //

  // const handleSaveToPC = psaux => {
  //   const fileData = psaux;
  //   const blob = new Blob([fileData], {type: "text/plain"});
  //   const url = URL.createObjectURL(blob);
  //   const link = document.createElement('a');
  //   link.download = 'filename.json';
  //   link.href = url;
  //   link.click();
  // }

  return (
    <>
      <Form>
        <Form.Field>
          <Input
            placeholder="IP adresa"
            value={ip}
            onChange={(e) => ipSet(e.target.value)}
          />
        </Form.Field>
        <Form.Field>
          <Input
            placeholder="Username"
            value={uname}
            onChange={(e) => unameSet(e.target.value)}
          />
        </Form.Field>
        <Form.Field>
          <Input
            placeholder="Password"
            value={pwd}
            onChange={(e) => pwdSet(e.target.value)}
          />
        </Form.Field>

        <Form.Field>
          <Button
            onClick={async () => {
              const request = { ip, uname, pwd };
              const response = await fetch("/request", {
                method: "PUT",
                headers: {
                  "Content-Type": "application/json",
                },
                body: JSON.stringify(request),
              });
              console.log(request);
              if (response.ok) {
                console.log("response worked!");
                ipSet("127.0.0.1");
                unameSet("ydrea");
                pwdSet("lorien");
              }
            }}
          >
            submit
          </Button>
        </Form.Field>
      </Form>
      {/* <Tab psaux={psaux} /> */}
      {/* <button onClick={() => handleSaveToPC()}>download</button> */}
      <TabelA psaux={psaux} load={load} />
      {/* <Bel data={data} /> */}
    </>
  );
};
