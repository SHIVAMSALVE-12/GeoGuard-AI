import api from "./api";

import type {
  PredictionResponse,
} from "../types/prediction";

export async function predictDamage(
  file: File,
): Promise<PredictionResponse> {

  const formData = new FormData();

  formData.append(
    "image",
    file,
  );

  const response = await api.post<PredictionResponse>(

    "/predict",

    formData,

    {
      headers: {
        "Content-Type":
          "multipart/form-data",
      },
    },

  );

  return response.data;
}