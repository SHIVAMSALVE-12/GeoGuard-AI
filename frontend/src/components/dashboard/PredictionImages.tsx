import { useState } from "react";

import {
  Card,
  CardContent,
  CardMedia,
  Dialog,
  DialogContent,
  Grid,
  IconButton,
  Typography,
} from "@mui/material";

import CloseIcon from "@mui/icons-material/Close";

type PredictionImagesProps = {
  original: string;
  prediction: string;
  overlay: string;
};

type SelectedImage = {
  title: string;
  src: string;
} | null;

export default function PredictionImages({
  original,
  prediction,
  overlay,
}: PredictionImagesProps) {

  const [selectedImage, setSelectedImage] =
    useState<SelectedImage>(null);

  const images = [
    {
      title: "Original Image",
      src: original,
    },
    {
      title: "AI Prediction",
      src: prediction,
    },
    {
      title: "Damage Overlay",
      src: overlay,
    },
  ];

  return (
    <>
      {/* ==========================================
          Section Heading
      ========================================== */}

      <Typography
        variant="h5"
        sx={{
          mt: 5,
          mb: 3,
          fontWeight: 700,
        }}
      >
        AI Visual Analysis
      </Typography>

      {/* ==========================================
          Image Cards
      ========================================== */}

      <Grid
        container
        spacing={3}
      >
        {images.map((image) => (
          <Grid
            key={image.title}
            size={{
              xs: 12,
              md: 4,
            }}
          >
            <Card
              sx={{
                height: "100%",
                borderRadius: 3,
                cursor: "pointer",
                transition: "0.3s",

                "&:hover": {
                  transform: "translateY(-6px)",
                  boxShadow: 8,
                },
              }}
              onClick={() =>
                setSelectedImage(image)
              }
            >
              <CardMedia
                component="img"
                image={image.src}
                alt={image.title}
                sx={{
                  height: 320,
                  objectFit: "contain",
                  backgroundColor: "#F8FAFC",
                  p: 2,
                  borderRadius: 2,
                }}
              />

              <CardContent>
                <Typography
                  variant="h6"
                  align="center"
                  sx={{
                    fontWeight: 700,
                  }}
                >
                  {image.title}
                </Typography>
              </CardContent>
            </Card>
          </Grid>
        ))}
      </Grid>

      {/* ==========================================
          Full Screen Viewer
      ========================================== */}

      <Dialog
        open={selectedImage !== null}
        onClose={() => setSelectedImage(null)}
        maxWidth="xl"
        fullWidth
      >
        <DialogContent
          sx={{
            position: "relative",
            backgroundColor: "#111",
            p: 2,
          }}
        >
          <IconButton
            onClick={() => setSelectedImage(null)}
            sx={{
              position: "absolute",
              top: 10,
              right: 10,
              color: "white",
              zIndex: 10,
            }}
          >
            <CloseIcon />
          </IconButton>

          {selectedImage && (
            <>
              <Typography
                variant="h5"
                align="center"
                sx={{
                  color: "white",
                  mb: 2,
                  fontWeight: 700,
                }}
              >
                {selectedImage.title}
              </Typography>

              <CardMedia
                component="img"
                image={selectedImage.src}
                alt={selectedImage.title}
                sx={{
                  width: "100%",
                  maxHeight: "80vh",
                  objectFit: "contain",
                }}
              />
            </>
          )}
        </DialogContent>
      </Dialog>
    </>
  );
}