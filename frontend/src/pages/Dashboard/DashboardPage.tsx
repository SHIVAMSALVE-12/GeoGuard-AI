import {
  Box,
  Stack,
  Typography,
} from "@mui/material";

import {
  Navigate,
  useLocation,
} from "react-router-dom";

import AssessmentCard from "../../components/dashboard/AssessmentCard";
import PredictionImages from "../../components/dashboard/PredictionImages";
import ReasoningPanel from "../../components/dashboard/ReasoningPanel";
import DamageStatistics from "../../components/dashboard/DamageStatistics";
import DownloadCenter from "../../components/dashboard/DownloadCenter";

import FadeIn from "../../components/common/FadeIn";

import type { PredictionResponse } from "../../types/prediction";

type DashboardState = {
  prediction: PredictionResponse;
  originalImage: string;
};

export default function DashboardPage() {
  const location = useLocation();

  const state = location.state as DashboardState | null;

  if (!state) {
    return <Navigate to="/assessment" replace />;
  }

  const result = state.prediction;
  console.log("Prediction Result:", result);
  console.log("Files:", result.files);
  console.log("Prediction Image:", result.files.prediction);
  console.log("Overlay Image:", result.files.overlay);
  
  const originalImage = state.originalImage;

  const assessment = result.assessment;

  const reasoning = result.reasoning;

  return (
    <Box>

      <Typography
        variant="h4"
        sx={{
          mb: 4,
          fontWeight: "bold",
        }}
      >
        AI Disaster Assessment Results
      </Typography>

      {/* ==========================================
          Assessment Cards
      ========================================== */}

      <FadeIn delay={0}>
        <Stack
          direction={{
            xs: "column",
            md: "row",
          }}
          spacing={3}
        >
          <Box sx={{ flex: 1 }}>
            <AssessmentCard
              title="Severity"
              value={assessment.severity}
              color="#2E7D32"
            />
          </Box>

          <Box sx={{ flex: 1 }}>
            <AssessmentCard
              title="Impact"
              value={assessment.impact}
              color="#1565C0"
            />
          </Box>

          <Box sx={{ flex: 1 }}>
            <AssessmentCard
              title="Confidence"
              value={`${assessment.confidence}%`}
              color="#ED6C02"
            />
          </Box>

          <Box sx={{ flex: 1 }}>
            <AssessmentCard
              title="Priority"
              value={reasoning.priority}
              color="#8E24AA"
            />
          </Box>
        </Stack>
      </FadeIn>

      {/* ==========================================
          Prediction Images
      ========================================== */}

      {result.files.prediction &&
        result.files.overlay && (
          <FadeIn delay={0.2}>
            <PredictionImages
              original={originalImage}
              prediction={result.files.prediction}
              overlay={result.files.overlay}
            />
          </FadeIn>
        )}

      {/* ==========================================
          AI Reasoning
      ========================================== */}

      <FadeIn delay={0.4}>
        <ReasoningPanel
          summary={reasoning.summary}
          analysis={reasoning.analysis}
          recommendations={
            reasoning.recommendations
          }
        />
      </FadeIn>

      {/* ==========================================
          Damage Statistics
      ========================================== */}

      <FadeIn delay={0.6}>
        <DamageStatistics
          damage={assessment.damage}
        />
      </FadeIn>

      {/* ==========================================
          Download Center
      ========================================== */}

      <FadeIn delay={0.8}>
        <DownloadCenter
          prediction={result.files.prediction}
          overlay={result.files.overlay}
          htmlReport={result.files.html_report}
          pdfReport={result.files.pdf_report}
        />
      </FadeIn>

    </Box>
  );
}