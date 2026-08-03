import { Button, CircularProgress } from "@mui/material";

type Props = {
  disabled: boolean;
  loading: boolean;
  onClick: () => void;
};

export default function RunAssessmentButton({
  disabled,
  loading,
  onClick,
}: Props) {
  return (
    <Button
      variant="contained"
      size="large"
      disabled={disabled || loading}
      onClick={onClick}
      sx={{
        mt: 4,
      }}
    >
      {loading ? (
        <>
          <CircularProgress
            size={22}
            color="inherit"
            sx={{ mr: 1 }}
          />
          Running AI...
        </>
      ) : (
        "Run AI Assessment"
      )}
    </Button>
  );
}