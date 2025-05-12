from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from application.services.statement_service import StatementService
from application.exporters.pdf_statement_exporter import PDFStatementExporter  # Import PDF exporter
from application.exporters.csv_statement_exporter import CSVStatementExporter  # Import CSV exporter
from application.dependencies import get_statement_service  # Import get_statement_service
import os  # Import os to handle directory creation

router = APIRouter(prefix="/statements")

class StatementRequest(BaseModel):
    account_id: str
    month: int
    year: int
    format: str  

@router.post("/generate")
def generate_statement(
    request: StatementRequest,
    service: StatementService = Depends(get_statement_service)
):
    try:
        statement = service.generate_statement(request.account_id, request.month, request.year)
        exporter = PDFStatementExporter() if request.format == "pdf" else CSVStatementExporter()
        
        # Ensure the 'statements' directory exists
        os.makedirs("statements", exist_ok=True)
        
        file_path = f"statements/{request.account_id}_{request.month}_{request.year}.{request.format}"
        exporter.export(statement, file_path)
        return {"message": f"Statement generated at {file_path}"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))