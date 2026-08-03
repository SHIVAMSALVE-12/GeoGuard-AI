import { Box, Typography } from "@mui/material";
import CloudUploadIcon from "@mui/icons-material/CloudUpload";
import { useDropzone } from "react-dropzone";

type UploadAreaProps = {
  onFileSelect: (file: File) => void;
};

export default function UploadArea({
  onFileSelect,
}: UploadAreaProps) {
  const { getRootProps, getInputProps, isDragActive } =
    useDropzone({
      multiple: false,

      accept: {
        "image/png": [".png"],
        "image/jpeg": [".jpg", ".jpeg"],
        "image/tiff": [".tif", ".tiff"],
      },

      onDrop: (acceptedFiles) => {
        if (acceptedFiles.length > 0) {
          onFileSelect(acceptedFiles[0]);
        }
      },
    });

  return (
    <Box
      {...getRootProps()}
      sx={{
        border: "2px dashed #1976d2",
        borderRadius: 3,
        p: 6,
        textAlign: "center",
        cursor: "pointer",
        transition: "0.3s",

        "&:hover": {
          backgroundColor: "#f5f7fa",
        },
      }}
    >
      <input {...getInputProps()} />

      <CloudUploadIcon
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
        {isDragActive
          ? "Drop image here..."
          : "Drag & Drop Image"}
      </Typography>

      <Typography
        color="text.secondary"
        sx={{
          mt: 2,
        }}
      >
        PNG • JPG • JPEG • TIFF
      </Typography>
    </Box>
  );
}