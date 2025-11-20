package ch.bfh.dsp4d.cli.command;

import ch.bfh.dsp4d.core.service.DocumentSummarizationService;
import io.quarkus.picocli.runtime.annotations.TopCommand;
import jakarta.inject.Inject;
import picocli.CommandLine;
import picocli.CommandLine.Command;
import picocli.CommandLine.Option;
import picocli.CommandLine.Parameters;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

/**
 * CLI command for document summarization experiments.
 *
 * This tool allows researchers to quickly test document processing
 * with different models and configurations from the command line.
 *
 * Examples:
 * <pre>
 * # Summarize a file
 * ./mvnw quarkus:dev -Dquarkus.args="summarize medical-report.txt"
 *
 * # Classify a document
 * ./mvnw quarkus:dev -Dquarkus.args="summarize --classify medical-report.txt"
 *
 * # Extract entities
 * ./mvnw quarkus:dev -Dquarkus.args="summarize --extract medical-report.txt"
 * </pre>
 */
@TopCommand
@Command(
    name = "summarize",
    mixinStandardHelpOptions = true,
    description = "Summarize, classify, or extract entities from medical documents"
)
public class SummarizeCommand implements Runnable {

    @Inject
    DocumentSummarizationService summarizationService;

    @Parameters(
        index = "0",
        description = "Path to the document file to process"
    )
    Path documentPath;

    @Option(
        names = {"-c", "--classify"},
        description = "Classify the document instead of summarizing"
    )
    boolean classify;

    @Option(
        names = {"-e", "--extract"},
        description = "Extract entities instead of summarizing"
    )
    boolean extractEntities;

    @Option(
        names = {"-v", "--verbose"},
        description = "Show processing time and statistics"
    )
    boolean verbose;

    @Override
    public void run() {
        try {
            // Read document content
            if (!Files.exists(documentPath)) {
                System.err.println("Error: File not found: " + documentPath);
                System.exit(1);
            }

            String content = Files.readString(documentPath);

            if (verbose) {
                System.out.println("Document: " + documentPath);
                System.out.println("Length: " + content.length() + " characters");
                System.out.println("---");
            }

            long startTime = System.currentTimeMillis();
            String result;

            // Process based on operation type
            if (classify) {
                result = summarizationService.classify(content);
            } else if (extractEntities) {
                result = summarizationService.extractEntities(content);
            } else {
                result = summarizationService.summarize(content);
            }

            long duration = System.currentTimeMillis() - startTime;

            // Output results
            System.out.println(result);

            if (verbose) {
                System.out.println("\n---");
                System.out.println("Processing time: " + duration + " ms");
            }

        } catch (IOException e) {
            System.err.println("Error reading file: " + e.getMessage());
            System.exit(1);
        } catch (Exception e) {
            System.err.println("Error processing document: " + e.getMessage());
            if (verbose) {
                e.printStackTrace();
            }
            System.exit(1);
        }
    }
}
