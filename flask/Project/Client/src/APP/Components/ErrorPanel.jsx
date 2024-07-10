function ErrorPanel(props) {
  const { eMsg = null } = props;

  if (!eMsg) {
    return null;
  }

  return (
    <div className="w3-panel w3-red">
      <h3>Error!</h3>
      <p>{eMsg}</p>
    </div>
  );
}

export default ErrorPanel;
