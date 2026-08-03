import {
  Card,
  CardContent,
  Typography,
} from "@mui/material";

import StatusChip from "./StatusChip";

type AssessmentCardProps = {
  title: string;
  value: string | number;
  color?: string;
};

export default function AssessmentCard({
  title,
  value,
  color = "primary.main",
}: AssessmentCardProps) {
  const isNumeric =
    typeof value === "number" ||
    !Number.isNaN(Number(value));

  return (
    <Card
      sx={{
        height: "100%",
        borderRadius: 3,
        transition: "0.3s",
        "&:hover": {
          transform: "translateY(-4px)",
          boxShadow: 6,
        },
      }}
    >
      <CardContent>

        <Typography
          variant="body2"
          sx={{
            color: "text.secondary",
            mb: 2,
            fontWeight: 500,
          }}
        >
          {title}
        </Typography>

        {isNumeric ? (
          <Typography
            variant="h4"
            sx={{
              fontWeight: 700,
              color,
            }}
          >
            {value}
          </Typography>
        ) : (
          <StatusChip
            value={String(value)}
          />
        )}

      </CardContent>
    </Card>
  );
}