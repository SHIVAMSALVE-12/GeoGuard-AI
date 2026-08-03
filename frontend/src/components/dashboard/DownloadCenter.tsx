import {
  Button,
  Card,
  CardContent,
  Divider,
  Stack,
  Typography,
} from "@mui/material";

import ImageIcon from "@mui/icons-material/Image";
import PublicIcon from "@mui/icons-material/Public";
import DescriptionIcon from "@mui/icons-material/Description";
import PictureAsPdfIcon from "@mui/icons-material/PictureAsPdf";
import DownloadIcon from "@mui/icons-material/Download";

type DownloadCenterProps = {
  prediction: string | null;
  overlay: string | null;
  htmlReport: string | null;
  pdfReport: string | null;
};

export default function DownloadCenter({
  prediction,
  overlay,
  htmlReport,
  pdfReport,
}: DownloadCenterProps) {
  const downloads = [
    {
      title: "Download Prediction Image",
      url: prediction,
      icon: <ImageIcon />,
    },
    {
      title: "Download Damage Overlay",
      url: overlay,
      icon: <PublicIcon />,
    },
    {
      title: "Download HTML Report",
      url: htmlReport,
      icon: <DescriptionIcon />,
    },
    {
      title: "Download PDF Report",
      url: pdfReport,
      icon: <PictureAsPdfIcon />,
    },
  ];

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
            mb: 3,
            fontWeight: 700,
          }}
        >
          📥 Download Center
        </Typography>

        <Divider sx={{ mb: 3 }} />

        <Stack spacing={2}>
          {downloads.map((item) => (
            <Button
  key={item.title}
  variant="contained"
  color="primary"
  fullWidth
  disabled={!item.url}
  startIcon={item.icon}
  endIcon={<DownloadIcon />}
  onClick={() => {
    if (item.url) {
      window.open(item.url, "_blank");
    }
  }}
  sx={{
    justifyContent: "space-between",
    py: 1.5,
    borderRadius: 2,
    textTransform: "none",
    fontWeight: 600,
  }}
>
  {item.title}
</Button>
          ))}
        </Stack>

      </CardContent>
    </Card>
  );
}