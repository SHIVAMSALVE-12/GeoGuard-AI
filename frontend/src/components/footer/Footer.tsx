import {
  Box,
  Container,
  Typography,
} from "@mui/material";

export default function Footer() {
  return (
    <Box
      sx={{
        mt: 6,
        py: 3,
        backgroundColor: "#ffffff",
        borderTop: "1px solid #e5e7eb",
      }}
    >
      <Container maxWidth="xl">
        <Typography
          align="center"
          color="text.secondary"
        >
          © 2026 GeoGuard AI • Developed by Shivam Salve
        </Typography>

        <Typography
          align="center"
          color="text.secondary"
          variant="body2"
          sx={{ mt: 1 }}
        >
          Powered by React • FastAPI • PyTorch • Gemma 2
        </Typography>
      </Container>
    </Box>
  );
}