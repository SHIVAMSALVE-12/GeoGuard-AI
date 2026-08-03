import { Link as RouterLink } from "react-router-dom";

import {
  AppBar,
  Box,
  Button,
  Container,
  Toolbar,
  Typography,
} from "@mui/material";

export default function Navbar() {
  return (
    <AppBar
      position="static"
      elevation={1}
    >
      <Container maxWidth="xl">
        <Toolbar
          disableGutters
          sx={{
            justifyContent: "space-between",
          }}
        >
          {/* Logo */}
          <Box
            sx={{
              display: "flex",
              alignItems: "center",
              gap: 1,
            }}
          >
            <Typography variant="h5">
              🌍
            </Typography>

            <Typography
              variant="h6"
              sx={{
                fontWeight: "bold",
              }}
            >
              GeoGuard AI
            </Typography>
          </Box>

          {/* Navigation */}
          <Box
            sx={{
              display: "flex",
              gap: 2,
            }}
          >
            <Button
              color="inherit"
              component={RouterLink}
              to="/"
            >
              Home
            </Button>

            <Button
              color="inherit"
              component={RouterLink}
              to="/assessment"
            >
              Assessment
            </Button>

            <Button
              color="inherit"
              component={RouterLink}
              to="/dashboard"
            >
              Dashboard
            </Button>

            <Button
              color="inherit"
              component={RouterLink}
              to="/about"
            >
              About
            </Button>
          </Box>
        </Toolbar>
      </Container>
    </AppBar>
  );
}