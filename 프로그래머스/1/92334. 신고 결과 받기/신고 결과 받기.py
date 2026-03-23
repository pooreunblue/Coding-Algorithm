def solution(id_list, report, k):
    answer = []
    report_dict = {}
    mails = {}
    for i in id_list:
        mails[i] = 0
    for r in report:
        reporter, reported = r.split()
        if reported not in report_dict:
            report_dict[reported] = []
        if reporter not in report_dict[reported]:
            report_dict[reported].append(reporter)
    suspended = [reported for reported, reporter in report_dict.items() if len(reporter) >= k]
    for suspended_user in suspended:
        for reporter in report_dict[suspended_user]:
            mails[reporter] += 1
    for k, v in mails.items():
        answer.append(v)
    return answer