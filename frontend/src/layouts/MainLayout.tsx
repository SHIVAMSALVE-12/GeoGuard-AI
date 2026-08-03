import {
  Box,
  Container,
} from "@mui/material";

import Footer from "../components/footer/Footer";
import Navbar from "../components/navbar/Navbar";

type MainLayoutProps = {
  children: React.ReactNode;
};

export default function MainLayout({
  children,
}: MainLayoutProps) {
  return (
    <Box
      sx={{
        minHeight: "100vh",
        display: "flex",
        flexDirection: "column",

        // Theme Background
        backgroundColor: "background.default",
      }}
    >
      <Navbar />

      <Container
        maxWidth="xl"
        sx={{
          flexGrow: 1,

          py: 5,

          // Better spacing on mobile
          px: {
            xs: 2,
            sm: 3,
            md: 4,
          },
        }}
      >
        {children}
      </Container>

      <Footer />
    </Box>
  );
}