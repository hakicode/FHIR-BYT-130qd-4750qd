import Cocoa
import Vision

func recognizeText(imagePath: String) {
    guard let image = NSImage(contentsOfFile: imagePath),
          let cgImage = image.cgImage(forProposedRect: nil, context: nil, hints: nil) else {
        print("Could not load image: \(imagePath)")
        return
    }

    let request = VNRecognizeTextRequest { request, error in
        guard let observations = request.results as? [VNRecognizedTextObservation] else { return }
        let recognizedText = observations.compactMap { observation in
            observation.topCandidates(1).first?.string
        }.joined(separator: "\n")
        print(recognizedText)
    }

    request.recognitionLevel = .accurate
    // Provide language hint for Vietnamese
    request.recognitionLanguages = ["vi-VN"]
    // request.usesLanguageCorrection = true

    let handler = VNImageRequestHandler(cgImage: cgImage, options: [:])
    do {
        try handler.perform([request])
    } catch {
        print("Error: \(error)")
    }
}

if CommandLine.arguments.count > 1 {
    let filePath = CommandLine.arguments[1]
    recognizeText(imagePath: filePath)
} else {
    print("Please provide an image path.")
}
