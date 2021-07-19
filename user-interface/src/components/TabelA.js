import Spinner from "./Spinner";
import React, { Fragment } from "react";
// import { Table } from "reactstrap";

// const columns = [{
//   dataField: 'PID',
//   text: 'Process ID',
// }, {
//   dataField: '%CPU',
//   text: 'Proc. Load'
// }, {
//   dataField: 'COMMAND',
//   text: 'Command',
//    formatter: (cell) => {
//     return <>{cell.map(label => <li>{label}</li>)}</>
//   },
// }];

export const TabelA = ({ psaux, load }) => {

  return load ? (<Spinner />) : (
    <>      
    
  return (
    {/* <Fragment>
      {columns.map(psaux => {
        return (
          <Table>
            <thead>
              <tr>
                <th>Name</th>
                {psaux.text.map(personAttendendance => {
                  return <th>{personAttendendance.date}</th>;
                })}
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>{psaux.text}</td>
                {person.Attendence.map(personAttendendance => {
                  return <td>{personAttendendance.attendence}</td>;
                })}
              </tr>
            </tbody>
          </Table>
        );
      })}
    </Fragment> */}
  );

      {JSON.stringify (psaux, null, 2 )}
      {/* {Object.fromEntries(psaux.trim().split('\n').map(s => s.split(' ')))} */}

    </>
  );
};
