package ch.bfh.dsp4d.core.service;

import dev.langchain4j.service.SystemMessage;
import dev.langchain4j.service.UserMessage;
import io.quarkiverse.langchain4j.RegisterAiService;
import jakarta.enterprise.context.ApplicationScoped;

/**
 * AI service for medical document summarization.
 *
 * This service demonstrates the core use case: doctors needing to quickly digest
 * medical reports and generate abstracts/classifications while maintaining
 * data sovereignty (local processing only).
 *
 * Research focus: How small can the model be while maintaining accuracy?
 */
@RegisterAiService
@ApplicationScoped
public interface DocumentSummarizationService {

    /**
     * Generate a concise summary of a medical document.
     *
     * @param documentContent the full text of the medical document
     * @return a concise summary suitable for quick review
     */
    @SystemMessage("""
        You are a medical document summarization assistant for doctors in Switzerland.
        Your role is to create concise, accurate summaries of medical reports that:
        - Highlight critical findings and diagnoses
        - Preserve medical terminology accurately
        - Maintain patient safety by not omitting important details
        - Follow Swiss medical documentation standards

        Always maintain professional medical language and focus on actionable information.
        """)
    @UserMessage("""
        Please summarize the following medical document concisely:

        {documentContent}

        Provide a summary that includes:
        1. Key findings
        2. Diagnosis/conclusions
        3. Recommended actions (if any)
        """)
    String summarize(String documentContent);

    /**
     * Classify a medical document by type and urgency.
     *
     * @param documentContent the document to classify
     * @return classification result (e.g., "Report Type: Lab Results, Urgency: Routine")
     */
    @SystemMessage("""
        You are a medical document classifier. Analyze documents and provide:
        - Document type (e.g., Lab Results, Radiology Report, Consultation Note, Discharge Summary)
        - Urgency level (Routine, Urgent, Critical)
        - Specialty (e.g., Cardiology, Oncology, General Practice)

        Be precise and consistent in your classifications.
        """)
    @UserMessage("""
        Classify this medical document:

        {documentContent}

        Respond in format:
        Document Type: [type]
        Urgency: [level]
        Specialty: [specialty]
        """)
    String classify(String documentContent);

    /**
     * Extract key medical entities from a document (diagnoses, medications, procedures).
     *
     * @param documentContent the document to analyze
     * @return extracted entities in structured format
     */
    @SystemMessage("""
        You are a medical entity extraction assistant. Extract and structure:
        - Diagnoses (ICD codes if mentioned)
        - Medications (including dosages)
        - Procedures/interventions
        - Vital signs and lab values

        Present information clearly and accurately.
        """)
    @UserMessage("""
        Extract key medical entities from this document:

        {documentContent}

        Structure the output as:
        Diagnoses: [list]
        Medications: [list with dosages]
        Procedures: [list]
        Key Values: [lab results, vitals]
        """)
    String extractEntities(String documentContent);
}
