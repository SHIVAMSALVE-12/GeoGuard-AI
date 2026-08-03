import {
  Card,
  CardContent,
  Typography,
} from "@mui/material";

export default function AboutPage() {
  return (
    <Card>
      <CardContent>
        <Typography
          variant="h4"
          sx={{
            fontWeight: 700,
            mb: 2,
          }}
        >
          About GeoGuard AI
        </Typography>

        <Typography color="text.secondary">
          GeoGuard AI is an AI-powered disaster damage
          assessment platform that combines computer
          vision, geospatial analysis, and Large Language
          Models to assist emergency response teams.
        </Typography>
      </CardContent>
    </Card>
  );
}