# DSP4D - LLM Size Optimization Research Project

**Research Question:** How small can an LLM be while still effectively processing sensitive data (medical, financial, legal) with RAG support?

This is a 3-month research project investigating optimal LLM sizes for handling sensitive data using Retrieval Augmented Generation (RAG).

## Project Structure

```
dsp4d-proj/
├── llm-core/          # Core AI services and business logic
│   └── DocumentSummarizationService - Medical document processing
├── llm-api/           # REST API endpoints
│   └── DocumentResource - HTTP endpoints for testing
├── llm-cli/           # CLI tool for experimentation
│   └── SummarizeCommand - Command-line interface
└── pom.xml            # Parent POM with multi-module configuration
```

## Technology Stack

- **Java 21** - Latest LTS version
- **Quarkus 3.29.3** - Cloud-native Java framework (latest stable)
- **LangChain4j 1.4.0.CR2** - LLM orchestration library (latest)
- **Maven** - Build and dependency management

## Prerequisites

### Required

1. **Java 21** (already installed)
   ```bash
   java -version
   # Should show: openjdk version "21.0.2"
   ```

2. **Maven 3.9.9** (already installed)
   ```bash
   mvn -version
   # Should show: Apache Maven 3.9.9
   ```

3. **Ollama** (for local LLM execution)
   ```bash
   # Install Ollama from https://ollama.ai/
   brew install ollama  # macOS

   # Start Ollama service
   ollama serve

   # Pull a small model for testing (3B parameters)
   ollama pull llama3.2:3b

   # Optional: Pull other models for research
   ollama pull llama3.2:1b   # Smallest (1B parameters)
   ollama pull llama3.2:7b   # Medium (7B parameters)
   ollama pull mistral       # Alternative model
   ```

### Optional (for provider comparison)

- **OpenAI API Key** - For GPT model comparison
- **Hugging Face API Token** - For alternative models

## Quick Start

### 1. Ensure Ollama is Running

**IMPORTANT:** Start Ollama before running the application:

```bash
# Start Ollama service (in a separate terminal)
ollama serve

# Pull the default model (if not already done)
ollama pull llama3.2:3b

# Verify Ollama is running
curl http://localhost:11434/api/tags
```

### 2. Build the Project

```bash
# Navigate to project root
cd /Users/chrigel/Documents/workspace/private/bfh/dsp4d/dsp4d-proj

# Build all modules
./mvnw clean install

# Or build without running tests
./mvnw clean install -DskipTests
```

### 3. Run the REST API

```bash
# Navigate to API module
cd llm-api

# Start in development mode (hot reload enabled)
../mvnw quarkus:dev
```

**The API will be available at:**
- **Swagger UI:** http://localhost:8080/swagger-ui
- **OpenAPI Spec:** http://localhost:8080/openapi
- **Health Check:** http://localhost:8080/health
- **Metrics:** http://localhost:8080/metrics

**Test the API:**

```bash
# Example: Summarize a medical document
curl -X POST http://localhost:8080/api/documents/summarize \
  -H "Content-Type: application/json" \
  -d '{
    "content": "Patient presents with acute chest pain radiating to left arm. ECG shows ST elevation in leads II, III, aVF. Troponin levels elevated at 2.5 ng/mL. Immediate cardiology consultation recommended."
  }'

# Example: Classify a document
curl -X POST http://localhost:8080/api/documents/classify \
  -H "Content-Type: application/json" \
  -d '{
    "content": "Lab Results - Complete Blood Count: WBC 12.5, RBC 4.2, Hemoglobin 13.8 g/dL, Platelets 250k. All values within normal range."
  }'
```

### 4. Run the CLI Tool

```bash
# Navigate to CLI module
cd llm-cli

# Create a sample medical document in the llm-cli directory
cat > test-document.txt << EOF
Patient: John Doe
Date: November 20, 2025
Physician: Dr. Smith

MEDICAL REPORT - CARDIOLOGY CONSULTATION

Chief Complaint:
Patient presents with intermittent chest pain and shortness of breath during physical activity.

History:
65-year-old male with history of hypertension and hyperlipidemia. Non-smoker. Family history of coronary artery disease.

Physical Examination:
Blood Pressure: 145/92 mmHg
Heart Rate: 78 bpm, regular
Lungs: Clear to auscultation bilaterally
Heart: Normal S1, S2, no murmurs

Diagnostic Tests:
- ECG: Normal sinus rhythm, no acute changes
- Lipid Panel: Total cholesterol 240 mg/dL, LDL 160 mg/dL, HDL 38 mg/dL
- Troponin: Negative

Diagnosis:
1. Stable angina pectoris
2. Hypertension, uncontrolled
3. Hyperlipidemia

Recommendations:
1. Start atorvastatin 40mg daily
2. Increase lisinopril to 20mg daily
3. Stress test scheduled for next week
4. Follow-up in 2 weeks
5. Lifestyle modifications: diet, exercise

Urgency: Routine follow-up required
EOF

# Start the CLI in dev mode
../mvnw quarkus:dev

# In the CLI prompt, press 'e' to edit command args and enter:
# test-document.txt

# Or run directly with arguments:
../mvnw quarkus:dev -Dquarkus.args="test-document.txt"

# Classify the document
../mvnw quarkus:dev -Dquarkus.args="--classify test-document.txt"

# Extract entities with verbose output
../mvnw quarkus:dev -Dquarkus.args="--extract --verbose test-document.txt"
```

**CLI Options:**
- `<documentPath>` - Path to the document file (required)
- `-c, --classify` - Classify the document instead of summarizing
- `-e, --extract` - Extract entities instead of summarizing
- `-v, --verbose` - Show processing time and statistics
- `-h, --help` - Show help message

## Configuration

### Configuration Structure

The project uses a **shared configuration** approach to eliminate duplication:

- **Shared:** `shared-config/application-shared.properties` - LLM provider settings, bean discovery, logging
- **API:** `llm-api/src/main/resources/application.properties` - REST API-specific settings (HTTP, CORS, OpenAPI)
- **CLI:** `llm-cli/src/main/resources/application.properties` - CLI-specific settings (disable HTTP server)

### Switching LLM Models

The project is configured for **Ollama by default** (local, data sovereignty compliant).

#### Change Ollama Model

Edit `shared-config/application-shared.properties`:

```properties
# Switch to a different model size
quarkus.langchain4j.ollama.chat-model.model-id=llama3.2:1b  # Smallest
# quarkus.langchain4j.ollama.chat-model.model-id=llama3.2:3b  # Default
# quarkus.langchain4j.ollama.chat-model.model-id=llama3.2:7b  # Larger
```

Then pull the model:
```bash
ollama pull llama3.2:1b
```

#### Using Environment Variables

You can override settings without editing files:

```bash
# Use a different model
export OLLAMA_MODEL=llama3.2:7b
../mvnw quarkus:dev

# Use a different Ollama instance
export OLLAMA_URL=http://192.168.1.100:11434
../mvnw quarkus:dev
```

#### Using OpenAI (Optional)

1. Add OpenAI dependency to both `llm-api/pom.xml` and `llm-cli/pom.xml`:
   ```xml
   <dependency>
       <groupId>io.quarkiverse.langchain4j</groupId>
       <artifactId>quarkus-langchain4j-openai</artifactId>
   </dependency>
   ```

2. Update `shared-config/application-shared.properties`:
   ```properties
   # Comment out Ollama config and add OpenAI
   quarkus.langchain4j.openai.api-key=${OPENAI_API_KEY}
   quarkus.langchain4j.openai.chat-model.model-name=gpt-4o-mini
   ```

3. Set API key:
   ```bash
   export OPENAI_API_KEY=sk-your-api-key-here
   ```

## Development Workflow

### Running Tests

```bash
# Run unit tests
./mvnw test

# Run integration tests
./mvnw verify

# Run tests for specific module
cd llm-core
../mvnw test
```

### Development Mode Features

Quarkus provides hot reload in dev mode:

```bash
cd llm-api
../mvnw quarkus:dev
```

- Edit Java files → automatic recompilation
- Edit config files → automatic restart
- Press `w` → open browser to Dev UI
- Press `h` → show dev mode help

### IntelliJ IDEA Run Configuration

The project includes IntelliJ run configurations in `.run/` directory:
- **API Dev Mode** - Run llm-api module in development mode
- **CLI Dev Mode** - Run llm-cli module
- **Build All** - Build all modules

### Adding New AI Services

1. Create interface in `llm-core/src/main/java/ch/bfh/dsp4d/core/service/`
2. Annotate with `@RegisterAiService` and `@ApplicationScoped`
3. Define methods with `@SystemMessage` and `@UserMessage`
4. Inject service in REST resources or CLI commands

Example:
```java
@RegisterAiService
@ApplicationScoped
public interface MyNewService {
    @SystemMessage("You are a helpful assistant...")
    @UserMessage("Process this: {input}")
    String process(String input);
}
```

## Research Use Cases

### Medical Document Summarization

**Goal:** Help doctors quickly digest medical reports after hours.

**Workflow:**
1. Load medical document (lab results, radiology reports, consultation notes)
2. Generate concise summary highlighting critical findings
3. Classify by type and urgency
4. Extract key entities (diagnoses, medications, procedures)

**Data Sovereignty:** All processing happens locally via Ollama - no data leaves the device.

### Model Size Evaluation

**Research Question:** What's the minimum model size for accurate medical document processing?

**Test Matrix:**
| Model Size | Example Models | Use Case |
|------------|---------------|----------|
| 1B params  | llama3.2:1b   | Simple classification |
| 3B params  | llama3.2:3b   | Standard summarization |
| 7B params  | llama3.2:7b   | Complex entity extraction |
| 13B params | llama3.2:13b  | High-accuracy clinical tasks |

## Troubleshooting

### Ollama Connection Issues

```bash
# Check if Ollama is running
curl http://localhost:11434/api/tags

# If not running, start it
ollama serve

# Verify model is pulled
ollama list
```

### Build Errors

```bash
# Clean build artifacts
./mvnw clean

# Update dependencies
./mvnw dependency:resolve

# Skip tests if failing
./mvnw clean install -DskipTests
```

### Port Already in Use

```bash
# API running on different port
cd llm-api
../mvnw quarkus:dev -Dquarkus.http.port=8081
```

## Next Steps

1. **Phase 3 (Current):** Experimental setup
   - ✅ Project structure created
   - ✅ Ollama integration configured
   - ⏳ Create golden test datasets
   - ⏳ Implement RAG with vector database

2. **Phase 4:** Run experiments
   - Test baseline models (no RAG)
   - Test RAG-enhanced models
   - Collect metrics (accuracy, latency, memory)

3. **Phase 5:** Analysis and documentation
   - Generate performance matrix
   - Identify sweet spots for different sensitivity levels
   - Write final report

## License

Research project for BFH (Bern University of Applied Sciences).
