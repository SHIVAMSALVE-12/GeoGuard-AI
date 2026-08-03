import Chip from "@mui/material/Chip";

type StatusChipProps = {
  value: string;
};

export default function StatusChip({
  value,
}: StatusChipProps) {
  const normalized = value.toLowerCase();

  let color:
    | "success"
    | "warning"
    | "error"
    | "info"
    | "default" = "default";

  let label = value;

  switch (normalized) {
    // Severity
    case "minimal":
      color = "success";
      label = "🟢 Minimal";
      break;

    case "low":
      color = "success";
      label = "🟢 Low";
      break;

    case "moderate":
      color = "warning";
      label = "🟠 Moderate";
      break;

    case "high":
      color = "error";
      label = "🔴 High";
      break;

    case "extreme":
      color = "error";
      label = "🟣 Extreme";
      break;

    // Impact
    case "limited":
      color = "info";
      label = "🔵 Limited";
      break;

    case "significant":
      color = "warning";
      label = "🟠 Significant";
      break;

    case "severe":
      color = "error";
      label = "🔴 Severe";
      break;

    case "catastrophic":
      color = "error";
      label = "🟣 Catastrophic";
      break;

    // Priority
    case "critical":
      color = "error";
      label = "🔴 Critical";
      break;

    default:
      color = "default";
      label = value;
  }

  return (
    <Chip
      label={label}
      color={color}
      variant="filled"
      size="medium"
      sx={{
        px: 1,
        py: 2.5,
        fontSize: "0.95rem",
        fontWeight: 700,
        borderRadius: 2,
        minWidth: 130,
      }}
    />
  );
}