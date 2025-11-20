package ch.bfh.dsp4d.api.resource;

import ch.bfh.dsp4d.core.service.DocumentSummarizationService;
import jakarta.inject.Inject;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.MediaType;
import org.eclipse.microprofile.openapi.annotations.Operation;
import org.eclipse.microprofile.openapi.annotations.tags.Tag;
import org.jboss.logging.Logger;

/**
 * REST endpoint for document processing operations.
 *
 * Provides HTTP access to AI-powered document summarization, classification,
 * and entity extraction services for research and evaluation purposes.
 */
@Path("/api/documents")
@Produces(MediaType.APPLICATION_JSON)
@Consumes(MediaType.APPLICATION_JSON)
@Tag(name = "Document Processing", description = "AI-powered document analysis endpoints")
public class DocumentResource {

    private static final Logger LOG = Logger.getLogger(DocumentResource.class);

    @Inject
    DocumentSummarizationService summarizationService;

    /**
     * Summarize a medical document.
     *
     * @param request the document content
     * @return summarization response
     */
    @POST
    @Path("/summarize")
    @Operation(
        summary = "Summarize document",
        description = "Generate a concise summary of a medical document highlighting key findings and recommendations"
    )
    public SummarizeResponse summarize(SummarizeRequest request) {
        LOG.infof("Summarizing document of length: %d characters", request.content.length());

        long startTime = System.currentTimeMillis();
        String summary = summarizationService.summarize(request.content);
        long duration = System.currentTimeMillis() - startTime;

        LOG.infof("Summarization completed in %d ms", duration);

        return new SummarizeResponse(summary, duration);
    }

    /**
     * Classify a medical document by type and urgency.
     *
     * @param request the document content
     * @return classification response
     */
    @POST
    @Path("/classify")
    @Operation(
        summary = "Classify document",
        description = "Classify a medical document by type, urgency level, and specialty"
    )
    public ClassifyResponse classify(ClassifyRequest request) {
        LOG.infof("Classifying document of length: %d characters", request.content.length());

        long startTime = System.currentTimeMillis();
        String classification = summarizationService.classify(request.content);
        long duration = System.currentTimeMillis() - startTime;

        LOG.infof("Classification completed in %d ms", duration);

        return new ClassifyResponse(classification, duration);
    }

    /**
     * Extract key medical entities from a document.
     *
     * @param request the document content
     * @return entity extraction response
     */
    @POST
    @Path("/extract-entities")
    @Operation(
        summary = "Extract entities",
        description = "Extract diagnoses, medications, procedures, and key values from medical documents"
    )
    public ExtractEntitiesResponse extractEntities(ExtractEntitiesRequest request) {
        LOG.infof("Extracting entities from document of length: %d characters", request.content.length());

        long startTime = System.currentTimeMillis();
        String entities = summarizationService.extractEntities(request.content);
        long duration = System.currentTimeMillis() - startTime;

        LOG.infof("Entity extraction completed in %d ms", duration);

        return new ExtractEntitiesResponse(entities, duration);
    }

    // DTOs
    public record SummarizeRequest(String content) {}
    public record SummarizeResponse(String summary, long processingTimeMs) {}

    public record ClassifyRequest(String content) {}
    public record ClassifyResponse(String classification, long processingTimeMs) {}

    public record ExtractEntitiesRequest(String content) {}
    public record ExtractEntitiesResponse(String entities, long processingTimeMs) {}
}
