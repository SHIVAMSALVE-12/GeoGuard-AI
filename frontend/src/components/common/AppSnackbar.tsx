import Alert from "@mui/material/Alert";
import Snackbar from "@mui/material/Snackbar";

type AppSnackbarProps = {
  open: boolean;
  message: string;
  severity: "success" | "error" | "warning" | "info";
  onClose: () => void;
};

export default function AppSnackbar({
  open,
  message,
  severity,
  onClose,
}: AppSnackbarProps) {
  return (
    <Snackbar
      open={open}
      autoHideDuration={4000}
      onClose={onClose}
      anchorOrigin={{
        vertical: "top",
        horizontal: "right",
      }}
    >
      <Alert
        onClose={onClose}
        severity={severity}
        variant="filled"
        sx={{
          width: "100%",
        }}
      >
        {message}
      </Alert>
    </Snackbar>
  );
}