import { createTheme } from "@mui/material/styles";

const theme = createTheme({
  palette: {
    mode: "light",

    primary: {
      main: "#1976D2",
    },

    secondary: {
      main: "#00ACC1",
    },

    success: {
      main: "#2E7D32",
    },

    warning: {
      main: "#ED6C02",
    },

    error: {
      main: "#D32F2F",
    },

    background: {
      default: "#F5F7FA",
      paper: "#FFFFFF",
    },
  },

  shape: {
    borderRadius: 12,
  },

  typography: {
    fontFamily: [
      "Inter",
      "Roboto",
      "Helvetica",
      "Arial",
      "sans-serif",
    ].join(","),

    h3: {
      fontWeight: 700,
    },

    h4: {
      fontWeight: 700,
    },

    h5: {
      fontWeight: 600,
    },

    h6: {
      fontWeight: 600,
    },

    body1: {
      fontWeight: 400,
    },

    body2: {
      fontWeight: 400,
    },

    button: {
      fontWeight: 600,
      textTransform: "none",
    },
  },

  components: {

    MuiCard: {

      styleOverrides: {

        root: {

          borderRadius: 16,

          boxShadow:
            "0px 6px 20px rgba(0,0,0,0.08)",

          transition: "0.3s",

          "&:hover": {

            transform: "translateY(-3px)",

            boxShadow:
              "0px 12px 28px rgba(0,0,0,0.12)",

          },

        },

      },

    },

    MuiButton: {

      styleOverrides: {

        root: {

          borderRadius: 10,

          paddingInline: 24,

          paddingBlock: 10,

          fontWeight: 600,

        },

      },

    },

    MuiPaper: {

      styleOverrides: {

        root: {

          borderRadius: 16,

        },

      },

    },

    MuiChip: {

      styleOverrides: {

        root: {

          fontWeight: 700,

          borderRadius: 10,

        },

      },

    },

  },

});

export default theme;