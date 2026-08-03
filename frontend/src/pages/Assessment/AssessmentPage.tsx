import { useEffect, useState } from "react";

import { useNavigate } from "react-router-dom";

import {
  Card,
  CardContent,
  Typography,
} from "@mui/material";

import UploadArea from "../../components/upload/UploadArea";
import ImagePreview from "../../components/upload/ImagePreview";
import RunAssessmentButton from "../../components/upload/RunAssessmentButton";
import AppSnackbar from "../../components/common/AppSnackbar";

import usePrediction from "../../hooks/usePrediction";

export default function AssessmentPage() {
  const navigate = useNavigate();

  const [file, setFile] =
    useState<File | null>(null);

  const [preview, setPreview] =
    useState("");

  const [snackbar, setSnackbar] = useState({
    open: false,
    message: "",
    severity: "success" as
      | "success"
      | "error"
      | "warning"
      | "info",
  });

  const {
    loading,
    error,
    runPrediction,
  } = usePrediction();

  function handleFile(
    selectedFile: File,
  ) {

    if (preview) {
      URL.revokeObjectURL(preview);
    }

    setFile(selectedFile);

    setPreview(
      URL.createObjectURL(selectedFile),
    );

  }

  async function handlePrediction() {

    if (!file) return;

    const prediction =
      await runPrediction(file);

    if (!prediction) return;

    setSnackbar({
      open: true,
      message:
        "Assessment completed successfully.",
      severity: "success",
    });

    navigate(
      "/dashboard",
      {
        state: {
          prediction,
          originalImage: preview,
        },
      },
    );

  }

  useEffect(() => {

    if (error) {

      setSnackbar({
        open: true,
        message: error,
        severity: "error",
      });

    }

  }, [error]);

  useEffect(() => {

    return () => {

      if (preview) {
        URL.revokeObjectURL(preview);
      }

    };

  }, [preview]);

  return (
    <>
      <Card
        sx={{
          borderRadius: 3,
        }}
      >
        <CardContent>

          <Typography
            variant="h4"
            sx={{
              mb: 4,
              fontWeight: 700,
            }}
          >
            Upload Disaster Image
          </Typography>

          <UploadArea
            onFileSelect={handleFile}
          />

          {preview && (
            <ImagePreview
              image={preview}
            />
          )}

          <RunAssessmentButton
            disabled={!file}
            loading={loading}
            onClick={handlePrediction}
          />

        </CardContent>
      </Card>

      <AppSnackbar
        open={snackbar.open}
        message={snackbar.message}
        severity={snackbar.severity}
        onClose={() =>
          setSnackbar((prev) => ({
            ...prev,
            open: false,
          }))
        }
      />
    </>
  );
}