import { useState } from "react";

import { predictDamage } from "../services/predictionService";

import type {
  PredictionResponse,
} from "../types/prediction";

export default function usePrediction() {

  const [loading, setLoading] =
    useState(false);

  const [result, setResult] =
    useState<PredictionResponse | null>(null);

  const [error, setError] =
    useState("");

  async function runPrediction(
    file: File,
  ): Promise<PredictionResponse | null> {

    try {

      setLoading(true);

      setError("");

      const prediction =
        await predictDamage(file);

      setResult(prediction);

      return prediction;

    }

    catch (err) {

      console.error(err);

      setError(
        "Failed to run AI assessment.",
      );

      return null;

    }

    finally {

      setLoading(false);

    }

  }

  return {

    loading,

    result,

    error,

    runPrediction,

  };

}