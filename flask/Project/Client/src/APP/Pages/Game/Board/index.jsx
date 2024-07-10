/* eslint-disable react/prop-types */

import { FaChessKnight, FaChessRook } from "react-icons/fa";

import axios from "axios";

import { useContext, useState } from "react";

import APPCONTEXT from "../../../Context/APPCONTEXT";

function Board(props) {
  const { board = [], setBoard = () => {}, getboard = () => {} } = props;
  // das
  return (
    <div>
      {board.map((row, i) => {
        return (
          <Row
            key={i}
            r={i}
            row={row}
            setBoard={setBoard}
            getboard={getboard}
          />
        );
      })}
    </div>
  );
}

function Row(props) {
  const { row = [], r = 0, setBoard = () => {}, getboard = () => {} } = props;

  const { token } = useContext(APPCONTEXT);

  const posibleMoves = (col, r, c) => {
    console.log(col, r, c);

    if (col === "X") {
      axios({
        method: "PUT",
        url: "http://127.0.0.1:9000/game/make-move",
        headers: {
          Authorization: `Bearer ${token}`,
        },
        data: {
          y: r,
          x: c,
        },
      }).then((res) => {
        getboard();
      });
      return;
    }

    axios({
      method: "get",
      url: "http://127.0.0.1:9000/game/possible-moves",
      headers: {
        Authorization: `Bearer ${token}`,
      },
    })
      .then((res) => {
        if (res?.data?.board) {
          setBoard(res?.data?.board);
        }
      })
      .catch((e) => {
        console.log(e);
      });
  };

  return (
    <div style={{ display: "flex" }}>
      {row.map((col, i) => {
        return (
          <div
            className="w3-border"
            key={i}
            style={{
              width: "60px",
              display: "flex",
              justifyContent: "center",
              cursor: "pointer",
              alignItems: "center",
              height: "60px",
              backgroundColor: (r + i) % 2 == 0 ? "red" : "black",
              opacity: col === "X" ? "0.5" : 1,
            }}
            onClick={() => posibleMoves(col, r, i)}
          >
            <Col value={col} />
          </div>
        );
      })}
    </div>
  );
}

function Col(props) {
  const { value } = props;

  if (value === "WR") {
    return (
      <span style={{ color: "white", fontSize: "40px" }}>
        <FaChessRook />
      </span>
    );
  }

  if (value === "BN") {
    return (
      <span style={{ color: "green", fontSize: "40px" }}>
        <FaChessKnight />
      </span>
    );
  }

  return null;
}

export default Board;
