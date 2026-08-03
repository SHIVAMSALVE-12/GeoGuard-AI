export interface Assessment {
  severity: string;

  impact: string;

  confidence: number;

  landcover: Record<string, number>;

  flood: Record<string, number>;

  damage: Record<string, number>;
}

export interface Reasoning {
  summary: string;

  analysis: string;

  priority: string;

  recommendations: string[];
}

export interface Files {
  prediction: string | null;

  overlay: string | null;

  html_report: string | null;

  pdf_report: string | null;
}

export interface PredictionResponse {
  success: boolean;

  message: string;

  assessment: Assessment;

  reasoning: Reasoning;

  files: Files;
}