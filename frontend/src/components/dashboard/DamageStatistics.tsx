import {
  Box,
  Card,
  CardContent,
  LinearProgress,
  Stack,
  Typography,
} from "@mui/material";

type DamageStatisticsProps = {
  damage: Record<string, number>;
};

const colors: Record<string, string> = {
  "No Damage": "#2E7D32",
  "Minor Damage": "#F9A825",
  "Major Damage": "#EF6C00",
  Destroyed: "#C62828",
};

export default function DamageStatistics({
  damage,
}: DamageStatisticsProps) {
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
            mb: 4,
            fontWeight: 700,
          }}
        >
          📊 Damage Statistics
        </Typography>

        <Stack spacing={3}>
          {Object.entries(damage).map(
            ([label, value]) => (
              <Box key={label}>

                <Box
                  sx={{
                    display: "flex",
                    justifyContent: "space-between",
                    mb: 1,
                  }}
                >
                  <Typography
                    sx={{
                      fontWeight: 600,
                    }}
                  >
                    {label}
                  </Typography>

                  <Typography>
                    {value.toFixed(2)}%
                  </Typography>
                </Box>

                <LinearProgress
                  variant="determinate"
                  value={Math.min(value, 100)}
                  sx={{
                    height: 12,
                    borderRadius: 10,

                    backgroundColor: "#ECEFF1",

                    "& .MuiLinearProgress-bar": {
                      backgroundColor:
                        colors[label],
                    },
                  }}
                />

              </Box>
            ),
          )}
        </Stack>

      </CardContent>
    </Card>
  );
}