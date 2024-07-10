import img404 from "./../Assets/404.png";

function NotFound() {
  return (
    <div className=" c_screen ">
      <img src={img404} style={{ width: "100%", height: "100%" }} />
    </div>
  );
}

export default NotFound;
