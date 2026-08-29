from client import GitNativeMultiFileRefactorPairProgrammerClient

def main():
    client = GitNativeMultiFileRefactorPairProgrammerClient()
    res = client.execute_git_refactoring('Migrate logging handlers from structlog to OpenTelemetry trace spans', 6)
    print('Git Refactor Commit: ' + res['refactor_commit_id'] + ' (' + res['git_commit_hash'][:8] + ')')
    print('Files Modified: ' + str(res['modified_files_count']) + ' | Tree-sitter Symbols: ' + str(res['tree_sitter_symbols_updated']))
    print('Diff Summary: ' + res['git_diff_summary'])
    print('Commit URL: ' + res['commit_permalink_url'])

if __name__ == '__main__':
    main()
