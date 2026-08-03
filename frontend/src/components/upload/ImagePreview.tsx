import { Box } from "@mui/material";

type ImagePreviewProps = {
  image: string;
};

export default function ImagePreview({
  image,
}: ImagePreviewProps) {
  return (
    <Box
      component="img"
      src={image}
      alt="Uploaded Preview"
      sx={{
        width: "100%",
        maxHeight: 400,
        objectFit: "contain",
        borderRadius: 3,
        mt: 3,
      }}
    />
  );
}