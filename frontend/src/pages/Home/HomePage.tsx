import {
  Box,
  Button,
  Card,
  CardContent,
  Grid,
  Typography,
} from "@mui/material";

import SatelliteAltIcon from "@mui/icons-material/SatelliteAlt";
import SmartToyIcon from "@mui/icons-material/SmartToy";
import DescriptionIcon from "@mui/icons-material/Description";
import { Link as RouterLink } from "react-router-dom";

export default function HomePage() {
  return (
    <Box>

      {/* ================= Hero ================= */}

      <Box
        sx={{
          textAlign: "center",
          py: 8,
        }}
      >
        <Typography
          variant="h2"
          sx={{
            fontWeight: 700,
            mb: 2,
          }}
        >
          🌍 GeoGuard AI
        </Typography>

        <Typography
          variant="h5"
          color="text.secondary"
          sx={{
            mb: 3,
          }}
        >
          AI Disaster Damage Assessment Platform
        </Typography>

        <Typography
          sx={{
            maxWidth: 700,
            mx: "auto",
            color: "text.secondary",
            mb: 5,
          }}
        >
          Analyze satellite imagery using Artificial Intelligence,
          assess disaster severity, generate AI-powered reasoning,
          and download professional assessment reports.
        </Typography>

        <Button
          component={RouterLink}
          to="/assessment"
          variant="contained"
          size="large"
        >
  Start Assessment
</Button>

      </Box>

      {/* ================= Feature Cards ================= */}

      <Grid
        container
        spacing={3}
      >

        <Grid size={{ xs: 12, md: 4 }}>
          <Card>
            <CardContent
              sx={{
                textAlign: "center",
              }}
            >
              <SatelliteAltIcon
                color="primary"
                sx={{
                  fontSize: 60,
                  mb: 2,
                }}
              />

              <Typography
                variant="h5"
                sx={{
                  fontWeight: 700,
                }}
              >
                AI Models
              </Typography>

              <Typography
                color="text.secondary"
              >
                Building damage assessment using
                transformer-based computer vision.
              </Typography>

            </CardContent>
          </Card>
        </Grid>

        <Grid size={{ xs: 12, md: 4 }}>
          <Card>
            <CardContent
              sx={{
                textAlign: "center",
              }}
            >
              <SmartToyIcon
                color="primary"
                sx={{
                  fontSize: 60,
                  mb: 2,
                }}
              />

              <Typography
                variant="h5"
                sx={{
                  fontWeight: 700,
                }}
              >
                Gemma AI
              </Typography>

              <Typography
                color="text.secondary"
              >
                Intelligent disaster reasoning,
                summaries, priorities,
                and recommendations.
              </Typography>

            </CardContent>
          </Card>
        </Grid>

        <Grid size={{ xs: 12, md: 4 }}>
          <Card>
            <CardContent
              sx={{
                textAlign: "center",
              }}
            >
              <DescriptionIcon
                color="primary"
                sx={{
                  fontSize: 60,
                  mb: 2,
                }}
              />

              <Typography
                variant="h5"
                sx={{
                  fontWeight: 700,
                }}
              >
                Reports
              </Typography>

              <Typography
                color="text.secondary"
              >
                Generate professional HTML
                and PDF disaster reports
                instantly.
              </Typography>

            </CardContent>
          </Card>
        </Grid>

      </Grid>

    </Box>
  );
}