import {
  Card,
  CardContent,
  Divider,
  List,
  ListItem,
  ListItemIcon,
  ListItemText,
  Typography,
} from "@mui/material";

import CheckCircleIcon from "@mui/icons-material/CheckCircle";

type ReasoningPanelProps = {
  summary: string;
  analysis: string;
  recommendations: string[];
};

export default function ReasoningPanel({
  summary,
  analysis,
  recommendations,
}: ReasoningPanelProps) {
  return (
    <Card
      sx={{
        mt: 5,
        borderRadius: 3,
      }}
    >
      <CardContent>

        <Typography
          variant="h5"
          sx={{
            fontWeight: 700,
            mb: 3,
          }}
        >
          🧠 AI Disaster Analysis
        </Typography>

        {/* Executive Summary */}

        <Typography
          variant="h6"
          sx={{
            fontWeight: 600,
            mb: 1,
          }}
        >
          Executive Summary
        </Typography>

        <Typography
          color="text.secondary"
          sx={{
            mb: 3,
          }}
        >
          {summary}
        </Typography>

        <Divider sx={{ mb: 3 }} />

        {/* Detailed Analysis */}

        <Typography
          variant="h6"
          sx={{
            fontWeight: 600,
            mb: 1,
          }}
        >
          Detailed Analysis
        </Typography>

        <Typography
          color="text.secondary"
          sx={{
            mb: 3,
            whiteSpace: "pre-line",
          }}
        >
          {analysis}
        </Typography>

        <Divider sx={{ mb: 3 }} />

        {/* Recommendations */}

        <Typography
          variant="h6"
          sx={{
            fontWeight: 600,
            mb: 2,
          }}
        >
          Emergency Recommendations
        </Typography>

        <List>
          {recommendations.map((recommendation, index) => (
            <ListItem
              key={index}
              disablePadding
              sx={{
                mb: 1,
              }}
            >
              <ListItemIcon>
                <CheckCircleIcon color="success" />
              </ListItemIcon>

              <ListItemText
                primary={recommendation}
              />
            </ListItem>
          ))}
        </List>

      </CardContent>
    </Card>
  );
}